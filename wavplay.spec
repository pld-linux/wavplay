Summary:	Play wav files under Linux
Summary(pl):	Odtwarzacz plików d¼wiêkowych wav pod Linuksa
Name:		wavplay
Version:	1.4
Release:	8
License:	GPL
Group:		Applications/Sound
URL:		http://www.vaxxine.com/ve3wwg/gnuwave.html
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/players/%{name}-%{version}.tar.gz
# Source0-md5:	726c58f47c0dbc3b58ff6c42300d518e
Patch0:		%{name}-make+res.patch
Patch1:		%{name}-X11.patch
Patch2:		%{name}-va_arg_fix.patch
Patch3:		%{name}-types.patch
Patch4:		%{name}-nonblock.patch
BuildRequires:	XFree86-devel
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Wavplay is a simple command-line tool that allows to play WAV audio
files under Linux.

%description -l pl
Wavplay jest prostym narzêdziem które pozwala odtwarzaæ pliki
d¼wiêkowe typu WAV pod Linuksem.

%package X11
Summary:	xltwavplay utility
Summary(pl):	Narzêdzie "xltwavplay"
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

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
%patch2
%patch3 -p1
%patch4 -p1

%build
%{__make} \
	CC=%{__cc} \
	OPT="%{rpmcflags}" \
	XLDOPTS="-L/usr/X11R6/%{_lib} -lXm -lXmu -lXt -lX11" \
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
%{_mandir}/man*/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xltwavplay
%{_appdefsdir}/xltwavplay
