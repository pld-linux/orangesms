#TODO
# - patch to sms.orangembox.txt - login and pasword from /etc/file or/and better from ~/.file
Summary:	orangesms
Summary(pl):	orangesms
Name:		orangesms
Version:	0.3
Release:	1.1
License:	BSD/Other
Group:		Applications
Source0:	http://rodion.infobot.pl/py/sms.orangembox.txt
# Source0-md5:	377ab4692d3f3ff3b9f22efd639a903f
Source1:	http://rodion.infobot.pl/py/tk.send.sms.txt
# Source1-md5:	547ea7324f6f38379d22679a9cfd44f5
Source2:	http://skrobul.bmj.pl/PyOrangeSMS.py
# Source2-md5:	6de5efb48f9317486bd7e075d4ff5b18
Patch0:		%{name}-shell.patch
URL:		http://rodion.infobot.pl/orangembox.php
Requires:	python >= 1:2.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMS script for Orange MBox.

%description -l pl
Skrypt SMS dla Orange MBox.

%package tk
Summary:	orangesms-tk
Summary(pl):	orangesms-tk
Group:		X11/Applications
Requires:	python >= 1:2.4.1
Requires:	tk

%description tk
Tk interface for orangesms.

%description tk -l pl
Interfejs dla orangesms napisany w Tk.

%prep
rm -rfd %{name}-%{version}
mkdir %{name}-%{version}
cp %{SOURCE0} ./%{name}-%{version}
cp %{SOURCE1} ./%{name}-%{version}
cp %{SOURCE2} ./%{name}-%{version}
%patch0 -p0
find '(' -name '*.txt' -o -name '*.py' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cd  %{name}-%{version}
install sms.orangembox.txt $RPM_BUILD_ROOT%{_bindir}/sms.orangembox.py
install tk.send.sms.txt $RPM_BUILD_ROOT%{_bindir}/tk.send.sms.py
install PyOrangeSMS.py $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sms.orangembox.py
%attr(755,root,root) %{_bindir}/PyOrangeSMS.py

%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tk.send.sms.py
