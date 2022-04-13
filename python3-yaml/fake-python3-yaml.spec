Name:           fake-python3-yaml
Version:        0.1.0
Release:        1
License:        MIT
Summary:        Fake provider
Group:          Fake
Source:         README.md
Requires:       python3-PyYAML
Provides:       python3-yaml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Ansible new-relic role requires python3-yaml, but OpenSuSE doesn't provide this
package.
In OpenSuSE python3-yaml package is called python3-PyYAML

%prep
%setup -c -T

%build
cp %{SOURCE0} README

%install

%files
%defattr(-,root,root)
%doc README

%changelog
* Tue Apr 12 2022 Marcin Morawski <marcin@morawskim.pl>
-  init package
