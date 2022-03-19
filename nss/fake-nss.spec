Name:           fake-nss
Version:        0.1.0
Release:        2
License:        MIT
Summary:        Fake provider
Group:          Fake
Source:         README.md
Requires:       libsoftokn3
Requires:       mozilla-nspr
Requires:       mozilla-nss
Provides:       nss = 3.75
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Responsively-App requires nss, but OpenSuSE doesn't provide this package.
In OpenSuSE nss package is called mozilla-nss

%prep
%setup -c -T

%build
cp %{SOURCE0} README

%install

%files
%defattr(-,root,root)
%doc README

%changelog
* Thu Apr 01 2021 Marcin Morawski <marcin@morawskim.pl>
-  init package
