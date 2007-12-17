%define	version  0.1.4
%define	release  %mkrel 4

Name:      manadic
Summary:   A dictionary for Mana
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://sourceforge.jp/projects/shinji/
Source0:   http://prdownloads.sourceforge.jp/shinji/15963/%{name}-%{version}.tar.bz2
Requires:      mana
BuildRequires: mana

%description
A dictionary for Mana.


%prep
%setup -q

%build
%configure2_5x

# (tv) disable parallel build (broken):
make

%install
rm -rf $RPM_BUILD_ROOT
# (tv) fix installing manarc:
perl -pi -e "s@ /usr/etc/@ $RPM_BUILD_ROOT/usr/etc/@" Makefile
mkdir -p $RPM_BUILD_ROOT/usr/etc/
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS* ChangeLog* COPYING* NEWS*
%doc README*
/usr/etc/manarc
/usr/lib/mana/dic/ipadic/*


