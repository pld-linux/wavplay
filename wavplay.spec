Summary:	wavplay - play wav files under Linux
Name:		wavplay
Version:	1.3
Release:	1
Copyright:	GPL
Group:		Applications/Sound
URL:		http://www.vaxxine.com/ve3wwg/gnuwave.html
Source:		ftp://sunsite.unc.edu/pub/Linux/apps/sound/players/wavplay-1.3.tar.gz
Patch0:		wavplay-1.3.patch
Patch1:		wavplay-install.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This version completely replaces wavplay-1.0 and its two patches.

%package X11
Summary: xltwavplay utility
Group: Applications/Sound

%description X11
The xltwavplay program now allows the user to point and click his way through
the playing of selected wav files, changing of options and performing
recordings.  

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
rm -rf $RPM_BUILD_ROOT
make "OPT=$RPM_OPT_FLAGS"

%install
install -d $RPM_BUILD_ROOT{%{_bindir},/usr/X11R6/bin,/usr/X11R6/lib/X11/app-defaults}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

make install

install wavplay.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo ".so wavplay.1" > $RPM_BUILD_ROOT%{_mandir}/man1/wavrec.1

gzip -9nf README* NEW BUGS $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc {README*,NEW,BUGS}.gz
%{_mandir}/man1/*.gz
%attr(755,root,root) %{_bindir}/wav*

%files X11
%defattr(644, root, root, 755)
%config /usr/X11R6/lib/X11/app-defaults/xltwavplay
%attr(755,root,root) /usr/X11R6/bin/xltwavplay
