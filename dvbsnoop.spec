Summary:	An open source DVB/MPEG analyzer
Name:		dvbsnoop
Version:	1.4.50
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/dvbsnoop/%{name}-%{version}.tar.gz
# Source0-md5:	68a5618c95b4372eea9ac5ec5005f299
URL:		http://dvbsnoop.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A DVB/MPEG stream analyzer program, which allows to watch (live)
stream information in human readable form. Its purpose is to debug,
dump or view digital stream information (e.g. digital television
broadcasts) send via satellite, cable or terrestrial. Streams can be
SI, PES or TS. Basically it can be described as a "swiss army knife"
analyzing program for DVB, MHP, DSM-CC or MPEG - similar to TCP
network sniffer programs like tcpdump. One may also analyze offline
MPEG streams, e.g. stored on DVD or MPEG2 movie files.
dvbsnoop is a command line based program. It's text output can be used
to for postprocessing via scripts or graphical analysis software like
MRTG or gnuplot.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
