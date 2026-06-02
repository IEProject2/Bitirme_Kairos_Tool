"""Build script for creating standalone executables and installers."""

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

# Colors for terminal output
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"


def log(message: str, color: str = BLUE) -> None:
    """Print colored log message."""
    print(f"{color}{message}{RESET}")


def error(message: str) -> None:
    """Print error message and exit."""
    print(f"{RED}Error: {message}{RESET}")
    sys.exit(1)


def success(message: str) -> None:
    """Print success message."""
    print(f"{GREEN}✓ {message}{RESET}")


def run_command(
    cmd: list[str],
    description: Optional[str] = None,
) -> int:
    """Run shell command and return exit code."""
    if description:
        log(description)
    log(f"$ {' '.join(cmd)}")
    return subprocess.call(cmd)


def build_cli_executable() -> None:
    """Build CLI executable using PyInstaller."""
    log("\n🔨 Building CLI executable...")

    spec_file = "factory_sim_cli.spec"
    if not Path(spec_file).exists():
        error(f"Spec file not found: {spec_file}")

    cmd = ["pyinstaller", spec_file, "--clean", "--onefile"]
    if sys.platform == "win32":
        cmd.append("--distpath=dist/cli")
    else:
        cmd.append("--distpath=dist/cli")

    if run_command(cmd, "Building CLI with PyInstaller...") != 0:
        error("PyInstaller CLI build failed")

    success("CLI executable built")


def build_gui_executable() -> None:
    """Build GUI executable using PyInstaller."""
    log("\n🔨 Building GUI executable...")

    spec_file = "factory_sim_gui.spec"
    if not Path(spec_file).exists():
        error(f"Spec file not found: {spec_file}")

    cmd = ["pyinstaller", spec_file, "--clean", "--onefile"]
    if sys.platform == "win32":
        cmd.append("--distpath=dist/gui")
    else:
        cmd.append("--distpath=dist/gui")

    if run_command(cmd, "Building GUI with PyInstaller...") != 0:
        error("PyInstaller GUI build failed")

    success("GUI executable built")


def create_windows_installer() -> None:
    """Create Windows installer using NSIS."""
    if sys.platform != "win32":
        log("⏭️  Skipping Windows installer (not on Windows)")
        return

    log("\n📦 Creating Windows installer...")

    nsis_script = "windows_installer.nsi"
    if not Path(nsis_script).exists():
        error(f"NSIS script not found: {nsis_script}")

    # Check if NSIS is installed
    makensis = shutil.which("makensis")
    if not makensis:
        error(
            "NSIS not found. Install from: "
            "https://nsis.sourceforge.io/Main_Page"
        )

    cmd = [makensis, nsis_script]
    if run_command(cmd, "Building installer with NSIS...") != 0:
        error("NSIS installer build failed")

    success("Windows installer created: dist/factory-sim-framework-installer.exe")


def create_macos_app() -> None:
    """Create macOS app bundle."""
    if sys.platform != "darwin":
        log("⏭️  Skipping macOS app bundle (not on macOS)")
        return

    log("\n📦 Creating macOS app bundle...")

    # PyInstaller should have already created the .app
    app_path = Path("dist/gui/factory-sim-gui.app")
    if not app_path.exists():
        error(f"App bundle not found: {app_path}")

    # Create a DMG (optional - requires additional tools)
    log("App bundle created at: dist/gui/factory-sim-gui.app")
    success("macOS app bundle ready for distribution")


def cleanup() -> None:
    """Clean up build artifacts."""
    log("\n🧹 Cleaning up build artifacts...")
    dirs_to_remove = ["build", "*.egg-info"]
    for pattern in dirs_to_remove:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                log(f"Removed: {path}")


def main() -> None:
    """Main build orchestration."""
    log(f"\n{'='*50}")
    log("Factory Sim Framework - Build Script")
    log(f"{'='*50}")

    # Check dependencies
    log("\n📋 Checking dependencies...")
    required_packages = ["pyinstaller", "click", "streamlit", "simpy", "plotly"]
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            success(f"{package} found")
        except ImportError:
            missing.append(package)

    if missing:
        error(
            f"Missing packages: {', '.join(missing)}\n"
            f"Install with: pip install -e '.[packaging]'"
        )

    # Build process
    try:
        build_cli_executable()
        build_gui_executable()
        create_windows_installer()
        create_macos_app()
        cleanup()

        log(f"\n{'='*50}")
        success("Build completed successfully!")
        log(f"{'='*50}\n")

        log("📦 Output locations:")
        log("  CLI:     dist/cli/")
        log("  GUI:     dist/gui/")
        if sys.platform == "win32":
            log("  Installer: dist/factory-sim-framework-installer.exe")

    except KeyboardInterrupt:
        error("Build cancelled by user")
    except Exception as e:
        error(f"Build failed: {e}")


if __name__ == "__main__":
    main()
