Summary:	KCM module to show info about system
Name:		about-distro
Version:	2.0.1
Release:	2
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	ninja

%description
KCM module to show info about system.

It can be customized by kcm-about-distrorc file in KDE config directory.

%files -f kcm-about-distro.lang
%{_libdir}/qt5/plugins/kcm_about_distro.so
%{_datadir}/kservices5/about-distro.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -G Ninja \
    -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

ninja

%install
DESTDIR="%{buildroot}" ninja -C build install

%find_lang kcm-about-distro
