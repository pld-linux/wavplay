Summary:	play wav files under Linux
Summary(pl):	Odtwarzacz plików d¼wiêkowe wav pod Linuksem
Name:		wavplay
Version:	1.4
Release:	3
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
URL:		http://www.vaxxine.com/ve3wwg/gnuwave.html
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/players/%{name}-%{version}.tar.gz
Patch0:		%{name}-make+res.patch
Patch1:		%{name}-X11.patch
BuildRequires:	XFree86-devel
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wavplay is a simple command-line tool that allows to play WAV audio
files under Linux.

%description -l pl
Wavplay jest prostym narzêdziem które pozwala odtwarzaæ pliki
d¼wiêkowe typu WAV pod Linuksem.

%package X11
Summary:	xltwavplay utility
Summary(pl):	Narzêdzie "xltwavplay"
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
Requires:	XFree86-libs

%description X11
The xltwavplay program now allows the user to point and click his way
through the playing of selected wav files, changing of options and
performing recordings.

%description X11 -l pl
Program xltwavplay pozwala u¿ytkownikowi szybko i ³atwo odgrywaæ
wybrane pliki wav, zmieniaæ ustawienia oraz nagrywaæ w³asne pliki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -rf $RPM_BUILD_ROOT
%{__make} \
	OPT="$RPM_OPT_FLAGS" \
	INSTDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/{bin,lib/X11/app-defaults}

%{__make} install \
	INSTDIR=$RPM_BUILD_ROOT%{_bindir} \
	XINSTDIR=$RPM_BUILD_ROOT%{_prefix}/X11R6/bin \
	RESDIR=$RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/app-defaults

install wavplay.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so wavplay.1" > $RPM_BUILD_ROOT%{_mandir}/man1/wavrec.1

gzip -9nf README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_mandir}/man*/*
%attr(755,root,root) %{_bindir}/wav*

%files X11
%defattr(644,root,root,755)
%config %{_prefix}/X11R6/lib/X11/app-defaults/xltwavplay
%attr(755,root,root) %{_prefix}/X11R6/bin/xltwavplay
