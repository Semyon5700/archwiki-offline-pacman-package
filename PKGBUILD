# Maintainer: Semyon5700 
pkgname=archwiki-offline-pacman-package
pkgver=1.0.0
pkgrel=1
pkgdesc="Offline ArchWiki access script - packaged version"
arch=('any')
url="https://github.com/Semyon5700/archwiki-offline-pacman-package"
license=('GPL3')
depends=('rofi' 'arch-wiki-docs')
source=("archwiki-offline"
        "arch-wiki-offline.desktop")
sha256sums=('SKIP'
            'SKIP')

package() {
    install -Dm755 "$srcdir/archwiki-offline" "$pkgdir/usr/bin/archwiki-offline"
    install -Dm644 "$srcdir/arch-wiki-offline.desktop" "$pkgdir/usr/share/applications/arch-wiki-offline.desktop"
}
