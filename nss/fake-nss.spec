Name:           fake-nss
Version:        0.1.0
Release:        3
License:        MIT
Summary:        Fake provider
Group:          Fake
Source:         README.md
Requires:       mozilla-nss
Provides:       nss = 3.99.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Lens requires nss, but OpenSuSE doesn't provide this package.
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
* Sun Feb 25 2024 Marcin Morawski <marcin@morawskim.pl>
-  Remove some required packages, update provided version

* Thu Apr 01 2021 Marcin Morawski <marcin@morawskim.pl>
-  init package
