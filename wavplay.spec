Summary:	Play WAV files under Linux
Summary(pl.UTF-8):	Odtwarzacz plików dźwiękowych WAV pod Linuksa
Name:		wavplay
Version:	1.4
Release:	12
License:	GPL
Group:		Applications/Sound
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/players/%{name}-%{version}.tar.gz
# Source0-md5:	726c58f47c0dbc3b58ff6c42300d518e
Patch0:		%{name}-make+res.patch
Patch1:		%{name}-X11.patch
Patch2:		%{name}-va_arg_fix.patch
Patch3:		%{name}-types.patch
Patch4:		%{name}-nonblock.patch
Patch5:		%{name}-WavOpenForWrite.patch
URL:		http://www.vaxxine.com/ve3wwg/gnuwave.html
BuildRequires:	motif-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir		/usr/share/X11/app-defaults

%description
Wavplay is a simple command-line tool that allows to play WAV audio
files under Linux.

%description -l pl.UTF-8
Wavplay jest prostym narzędziem które pozwala odtwarzać pliki
dźwiękowe typu WAV pod Linuksem.

%package X11
Summary:	xltwavplay utility
Summary(pl.UTF-8):	Narzędzie "xltwavplay"
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXt >= 1.0.0

%description X11
The xltwavplay program now allows the user to point and click his way
through the playing of selected WAV files, changing of options and
performing recordings.

%description X11 -l pl.UTF-8
Program xltwavplay pozwala użytkownikowi szybko i łatwo odgrywać
wybrane pliki WAV, zmieniać ustawienia oraz nagrywać własne pliki.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	XLDOPTS="-lXm -lXmu -lXt -lX11" \
	INSTDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_appdefsdir}}

%{__make} install \
	INSTDIR=$RPM_BUILD_ROOT%{_bindir} \
	XINSTDIR=$RPM_BUILD_ROOT%{_bindir} \
	RESDIR=$RPM_BUILD_ROOT%{_appdefsdir}

install wavplay.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so wavplay.1" > $RPM_BUILD_ROOT%{_mandir}/man1/wavrec.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS
%attr(755,root,root) %{_bindir}/wav*
%{_mandir}/man1/wav*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xltwavplay
%{_appdefsdir}/xltwavplay
