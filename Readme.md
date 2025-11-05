# ArchWiki Offline Pacman Package

A fork of the original ArchWiki Offline Access Script, packaged as an official Arch Linux pacman package for easy installation and maintenance.

## About

This project is a pacman package version of the original [ArchWiki Offline Access Script](https://github.com/niksingh710/archwiki-offline) by Nikhil Singh. It provides the same functionality but is distributed as a proper Arch Linux package for seamless integration with the system.

## Original Author

- **Nikhil Singh** - Original creator of ArchWiki Offline Access Script

## Fork Maintainer

- **Semyon5700** - Package maintainer and fork author

## Features

- **Official Package**: Distributed as a proper pacman package
- **Offline ArchWiki Access**: Browse ArchWiki documentation without internet connection
- **Multiple Display Modes**: Support for rofi, dmenu, and fzf
- **Flexible Openers**: Compatible with xdg-open, firefox, chromium, w3m, and other applications
- **System Integration**: Seamlessly integrates with Arch Linux package management

## Installation

### download pacman package in releases and install and

2. Clone and build the package:
```bash
git clone https://github.com/Semyon5700/archwiki-offline-pacman-package.git
cd archwiki-offline-pacman-package
makepkg -si
```

## Usage

After installation, you can use the script directly:

```bash
archwiki-offline [FLAGS]
```

### Flags

- `-h`: Display help information
- `-d`: Disown the process
- `-m MODE`: Select display mode (rofi, dmenu, or fzf)
- `-o OPENER`: Specify link opener (xdg-open, firefox, chromium, w3m, etc.)

## Package Benefits

- **Automatic Updates**: Receive updates through standard system updates
- **Dependency Management**: Automatic handling of required dependencies
- **Clean Removal**: Easy uninstallation without leaving files behind
- **System Integration**: Proper file placement and permission handling

## Documentation

For detailed usage instructions, display mode configurations, and tips, refer to the original project documentation. The functionality remains identical to the original script but with improved packaging.

## License

This project is licensed under the GPL 3.0 License. The original work by Nikhil Singh remains under the MIT License.

See the `LICENSES` file for complete licensing information.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements related to packaging and distribution.

## Acknowledgments

- Original ArchWiki Offline Access Script by Nikhil Singh
- arch-wiki-docs project for providing the offline documentation backbone
- Arch Linux community for packaging guidelines and support
