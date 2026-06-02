; NSIS Installer for Factory Sim Framework
; This script creates a professional Windows installer

!include "MUI2.nsh"
!include "x64.nsh"

; Name and file
Name "Factory Sim Framework"
OutFile "dist\factory-sim-framework-installer.exe"

; Default installation folder
InstallDir "$PROGRAMFILES\FactorySimFramework"

; Request application privileges for Windows Vista and higher
RequestExecutionLevel admin

; ===== MUI Settings =====
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

; Installer sections
Section "Install"
  SetOutPath "$INSTDIR"

  ; Copy CLI executable
  File "dist\cli\factory-sim-cli.exe"

  ; Copy GUI executable
  File "dist\gui\factory-sim-gui.exe"

  ; Copy documentation
  File "README.md"
  File "LICENSE"

  ; Create program group and shortcuts
  CreateDirectory "$SMPROGRAMS\Factory Sim Framework"
  CreateShortcut "$SMPROGRAMS\Factory Sim Framework\Factory Sim CLI.lnk" "$INSTDIR\factory-sim-cli.exe"
  CreateShortcut "$SMPROGRAMS\Factory Sim Framework\Factory Sim GUI.lnk" "$INSTDIR\factory-sim-gui.exe"
  CreateShortcut "$SMPROGRAMS\Factory Sim Framework\Uninstall.lnk" "$INSTDIR\uninstall.exe"

  ; Create desktop shortcuts (optional)
  CreateShortcut "$DESKTOP\Factory Sim GUI.lnk" "$INSTDIR\factory-sim-gui.exe"

  ; Write uninstaller
  WriteUninstaller "$INSTDIR\uninstall.exe"

  ; Add to Add/Remove Programs
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FactorySimFramework" \
                   "DisplayName" "Factory Sim Framework"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FactorySimFramework" \
                   "UninstallString" "$INSTDIR\uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FactorySimFramework" \
                   "DisplayVersion" "0.1.0"

SectionEnd

; Uninstaller section
Section "Uninstall"
  ; Remove files
  Delete "$INSTDIR\factory-sim-cli.exe"
  Delete "$INSTDIR\factory-sim-gui.exe"
  Delete "$INSTDIR\README.md"
  Delete "$INSTDIR\LICENSE"
  Delete "$INSTDIR\uninstall.exe"

  ; Remove shortcuts
  RMDir /r "$SMPROGRAMS\Factory Sim Framework"
  Delete "$DESKTOP\Factory Sim GUI.lnk"

  ; Remove directory
  RMDir "$INSTDIR"

  ; Remove registry entries
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FactorySimFramework"

SectionEnd
