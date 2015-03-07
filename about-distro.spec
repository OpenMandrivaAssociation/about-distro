Summary:	KCM module to show info about system
Name:		about-distro
Version:	2.0.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5ConfigWidgets)

%description
KCM module to show info about system.

It can be customized by kcm-about-distrorc file in KDE config directory.

%files -f kcm-about-distro.lang
%{_kde_libdir}/kde4/kcm_about_distro.so
%{_kde_services}/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

%find_lang kcm-about-distro
