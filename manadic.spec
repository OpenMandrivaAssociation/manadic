Summary:	A dictionary for Mana
Name:		manadic
Version:	0.1.4
Release:	13
Group:		System/Internationalization
License:	GPLv2
Url:		http://sourceforge.jp/projects/shinji/
Source0:	http://prdownloads.sourceforge.jp/shinji/15963/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	mana
Requires:	mana

%description
A dictionary for Mana.

%prep
%setup -q

%build
%configure2_5x

# (tv) disable parallel build (broken):
make

%install
# (tv) fix installing manarc:
sed -i -e "s@ /usr/etc/@ %{buildroot}/usr/etc/@" Makefile
mkdir -p %{buildroot}/usr/etc/
%makeinstall_std

%files
%doc AUTHORS* ChangeLog* COPYING* NEWS*
%doc README*
/usr/etc/manarc
/usr/lib/mana/dic/ipadic/*

