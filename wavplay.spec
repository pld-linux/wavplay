Summary:	play wav files under Linux
Summary(pl):	Odtwarzacz plik�w d�wi�kowych wav pod Linuksa
Name:		wavplay
Version:	1.4
Release:	6
License:	GPL
Group:		Applications/Sound
URL:		http://www.vaxxine.com/ve3wwg/gnuwave.html
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/players/%{name}-%{version}.tar.gz
Patch0:		%{name}-make+res.patch
Patch1:		%{name}-X11.patch
Patch2:		%{name}-va_arg_fix.patch
Patch3:		%{name}-types.patch
BuildRequires:	XFree86-devel
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wavplay is a simple command-line tool that allows to play WAV audio
files under Linux.

%description -l pl
Wavplay jest prostym narz�dziem kt�re pozwala odtwarza� pliki
d�wi�kowe typu WAV pod Linuksem.

%package X11
Summary:	xltwavplay utility
Summary(pl):	Narz�dzie "xltwavplay"
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}
Requires:	XFree86-libs

%description X11
The xltwavplay program now allows the user to point and click his way
through the playing of selected wav files, changing of options and
performing recordings.

%description X11 -l pl
Program xltwavplay pozwala u�ytkownikowi szybko i �atwo odgrywa�
wybrane pliki wav, zmienia� ustawienia oraz nagrywa� w�asne pliki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2
%patch3 -p1

%build
%{__make} \
	CC=%{__cc} \
	OPT="%{rpmcflags}" \
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS
%{_mandir}/man*/*
%attr(755,root,root) %{_bindir}/wav*

%files X11
%defattr(644,root,root,755)
%config %{_prefix}/X11R6/lib/X11/app-defaults/xltwavplay
%attr(755,root,root) %{_prefix}/X11R6/bin/xltwavplay
