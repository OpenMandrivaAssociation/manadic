%define	version  0.1.4
%define	release  %mkrel 11

Name:      manadic
Summary:   A dictionary for Mana
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://sourceforge.jp/projects/shinji/
Source0:   http://prdownloads.sourceforge.jp/shinji/15963/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
# (tv) fix installing manarc:
perl -pi -e "s@ /usr/etc/@ %{buildroot}/usr/etc/@" Makefile
mkdir -p %{buildroot}/usr/etc/
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc AUTHORS* ChangeLog* COPYING* NEWS*
%doc README*
/usr/etc/manarc
/usr/lib/mana/dic/ipadic/*


