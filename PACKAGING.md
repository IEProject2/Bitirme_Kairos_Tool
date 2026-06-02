# Standalone Application Packaging Guide

This guide explains how to build standalone executables and installers for Factory Sim Framework.

## Overview

Factory Sim Framework provides both CLI and GUI interfaces that can be packaged as standalone applications:

- **CLI**: Command-line interface using Click (for advanced users and automation)
- **GUI**: Web-based interface using Streamlit (for interactive use)

## System Requirements

### Development Requirements
- Python 3.11+
- pip and virtual environment

### For Building Executables
- PyInstaller: Cross-platform executable builder
- Platform-specific tools:
  - **Windows**: NSIS (Nullsoft Scriptable Install System)
  - **macOS**: Xcode Command Line Tools

## Installation

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Development & Packaging Dependencies
```bash
pip install -e ".[packaging]"
```

This installs:
- PyInstaller for creating executables
- All runtime dependencies (click, streamlit, simpy, plotly)

### 3. Install Platform-Specific Tools

#### Windows - Install NSIS
1. Download NSIS from: https://nsis.sourceforge.io/Download
2. Run the installer
3. Add NSIS to your PATH (usually `C:\Program Files (x86)\NSIS`)

#### macOS - Install Xcode Tools
```bash
xcode-select --install
```

## Building

### Quick Build (Both CLI & GUI)
```bash
python build_executable.py
```

This automatically:
1. ✓ Checks all dependencies
2. ✓ Builds CLI executable
3. ✓ Builds GUI executable
4. ✓ Creates Windows installer (on Windows)
5. ✓ Creates macOS app bundle (on macOS)

### Build Individual Components

#### Build CLI Only
```bash
pyinstaller factory_sim_cli.spec --clean --onefile --distpath=dist/cli
```

Output: `dist/cli/factory-sim-cli.exe` (Windows) or `dist/cli/factory-sim-cli` (macOS/Linux)

#### Build GUI Only
```bash
pyinstaller factory_sim_gui.spec --clean --onefile --distpath=dist/gui
```

Output: `dist/gui/factory-sim-gui.exe` (Windows) or `dist/gui/factory-sim-gui` (macOS/Linux)

#### Create Windows Installer
```bash
makensis windows_installer.nsi
```

Output: `dist/factory-sim-framework-installer.exe`

## Customizing the Build

### Update Application Metadata

**For CLI** (`factory_sim/cli.py`):
```python
@click.group()
@click.version_option(version="0.1.0")
def main() -> None:
    """Factory Sim Framework - Production scheduling and simulation."""
```

**For GUI** (`factory_sim/gui.py`):
```python
st.set_page_config(
    page_title="Factory Sim Framework",
    page_icon="🏭",
)
```

### Add Application Icon

1. Create a 256×256 PNG icon file
2. Convert to ICO (Windows) or ICNS (macOS):
   ```bash
   # Using PIL
   from PIL import Image
   img = Image.open("icon.png")
   img.save("icon.ico")
   ```
3. Update spec files:
   ```python
   exe = EXE(
       ...,
       icon="path/to/icon.ico",
   )
   ```

### Modify Windows Installer

Edit `windows_installer.nsi`:
- Change installer name: `OutFile "dist\..."`
- Change default install path: `InstallDir "..."`
- Add/remove shortcuts
- Customize welcome page

## Distribution

### Windows

**Standalone Executable**:
- Location: `dist/cli/factory-sim-cli.exe` and `dist/gui/factory-sim-gui.exe`
- No installation required
- Can be run from any directory
- Requires Windows 7 or later

**Installer**:
- Location: `dist/factory-sim-framework-installer.exe`
- Double-click to install
- Creates Start Menu shortcuts
- Adds uninstall entry to Control Panel
- Professional distribution method

### macOS

**Standalone Executable**:
- Location: `dist/cli/factory-sim-cli` and `dist/gui/factory-sim-gui`
- Make executable: `chmod +x dist/cli/factory-sim-cli`
- Run: `./dist/cli/factory-sim-cli` or `./dist/gui/factory-sim-gui`

**App Bundle**:
- Location: `dist/gui/factory-sim-gui.app`
- Double-click to run GUI
- Can create DMG for distribution:
  ```bash
  hdiutil create -volname "FactorySimFramework" \
    -srcfolder dist/gui/ \
    -ov -format UDZO factory-sim-framework.dmg
  ```

## Testing Executables

### Test CLI
```bash
# Windows
dist/cli/factory-sim-cli.exe --help
dist/cli/factory-sim-cli.exe run --help

# macOS/Linux
./dist/cli/factory-sim-cli --help
./dist/cli/factory-sim-cli run --help
```

### Test GUI
```bash
# Windows
dist/gui/factory-sim-gui.exe

# macOS/Linux
./dist/gui/factory-sim-gui
```

Browser should open at: `http://localhost:8501`

## Troubleshooting

### "ModuleNotFoundError" in Executable
**Problem**: Missing module when running built executable

**Solution**:
1. Add to `hiddenimports` in spec file
2. Rebuild: `pyinstaller --clean <spec_file>`

### "NSIS not found" Error
**Problem**: Can't create Windows installer

**Solution**:
1. Install NSIS from https://nsis.sourceforge.io/
2. Ensure it's in PATH
3. Verify: `where makensis` (Windows) or `which makensis` (macOS/Linux)

### Large Executable Size
**Problem**: Built executable is too large

**Solution**:
- Use `--onefile` flag (already configured)
- Remove unnecessary dependencies
- Use UPX compression (if needed):
  ```bash
  pyinstaller --upx-dir=/path/to/upx <spec_file>
  ```

### GUI Won't Display
**Problem**: Streamlit GUI closes immediately

**Solution**:
1. Check for errors: Run from command line to see output
2. Ensure Streamlit dependencies are in hiddenimports
3. Rebuild with: `pyinstaller --clean factory_sim_gui.spec`

## File Structure After Build

```
dist/
├── cli/
│   └── factory-sim-cli[.exe]
├── gui/
│   └── factory-sim-gui[.exe]  (or .app on macOS)
└── factory-sim-framework-installer.exe  (Windows only)
```

## Advanced Options

### Create 32-bit vs 64-bit Executables

**For 64-bit only**:
```python
# In spec file, NSIS:
platform = "x64"
```

**For both**:
Build twice with different Python installations or use `--platform` in PyInstaller.

### Add Runtime Arguments

To pass arguments when running executable:

**CLI**:
```bash
factory-sim-cli run config.json --output results.json
```

**GUI**:
```bash
factory-sim-gui --logger.level=debug
```

## Release Checklist

- [ ] Update version in `pyproject.toml` and `factory_sim/cli.py`
- [ ] Test executables on target platforms
- [ ] Update installer graphics (optional)
- [ ] Run security scan on executables
- [ ] Create release notes
- [ ] Upload to distribution platform
- [ ] Update documentation with download links

## Resources

- [PyInstaller Documentation](https://pyinstaller.readthedocs.io/)
- [NSIS Documentation](https://nsis.sourceforge.io/Docs/)
- [Streamlit Deployment Guide](https://docs.streamlit.io/library/deploy)
- [Click Documentation](https://click.palletsprojects.com/)
