Name:		manadic
Summary:	A dictionary for Mana
Version:	0.1.4
Release:	13
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.jp/projects/shinji/
Source0:	http://prdownloads.sourceforge.jp/shinji/15963/%{name}-%{version}.tar.bz2
BuildRequires:	mana
Requires:	mana
BuildArch:	noarch

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
perl -pi -e "s@ /usr/etc/@ %{buildroot}/usr/etc/@" Makefile
mkdir -p %{buildroot}/usr/etc/
%makeinstall_std

%files
%doc AUTHORS* ChangeLog* COPYING* NEWS*
%doc README*
/usr/etc/manarc
/usr/lib/mana/dic/ipadic/*

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-11mdv2011.0
+ Revision: 666378
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-10mdv2011.0
+ Revision: 606627
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-9mdv2010.1
+ Revision: 523256
- rebuilt for 2010.1

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.4-8mdv2010.0
+ Revision: 423704
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-7mdv2009.0
+ Revision: 223149
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-6mdv2008.1
+ Revision: 152900
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-5mdv2008.1
+ Revision: 152899
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat May 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.1.4-4mdv2008.0
+ Revision: 31250
- rebuild for new era
- rebuild for new era


* Mon May 15 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.1.4-2mdk
- fix file list for x86_64

* Tue May 09 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.1.4-1mdk
- disable parallel build (broken)
- fix install
- first spec for Mandriva (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

