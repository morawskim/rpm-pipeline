Name:           fluent-bit
Version:        1.9.2
Release:        1
Summary:        Fast Log Processor and Forwarder
License:        Apache-2.0
URL:            https://github.com/fluent/fluent-bit
Source:         https://github.com/fluent/fluent-bit/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        fluent-bit.service
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libsystemd)

%description
Fluent Bit is a fast Log Processor and Forwarder. Its part of the Fluentd Ecosystem and a CNCF sub-project.
Fluent Bit allows to collect log events or metrics from different sources, process them and deliver them to different backends such as Fluentd, Elasticsearch, NATS, InfluxDB or any custom HTTP end-point within others.
In addition, Fluent Bit comes with full Stream Processing capabilities: data manipulation and analytics using SQL queries.

%prep
%setup -q

%build
%define _lto_cflags %{nil}
%cmake -Wno-dev \
          -DBUILD_SHARED_LIBS=OFF \
          -DFLB_DEBUG=Off \
          -DFLB_TRACE=Off \
          -DFLB_RELEASE=On \
          -DFLB_JEMALLOC=On \
          -DFLB_TLS=On \
          -DFLB_SHARED_LIB=Off \
          -DFLB_EXAMPLES=Off \
          -DFLB_HTTP_SERVER=On \
          -DFLB_IN_SYSTEMD=On \
          -DFLB_IN_CPU=On \
          -DFLB_IN_MEM=On \
          -DFLB_IN_SYSLOG=On \
          -DFLB_OUT_ES=On
%cmake_build

%install
%cmake_install
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/fluent-bit
%{__install} -m644 conf/parsers_*.conf %{buildroot}/%{_sysconfdir}/fluent-bit
%{__mv} %{buildroot}%{_prefix}/%{_sysconfdir}/fluent-bit/* %{buildroot}/%{_sysconfdir}/fluent-bit
%{__rm} -fr %{buildroot}%{_prefix}/%{_sysconfdir}/fluent-bit
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__cp} %{S:1} %{buildroot}%{_unitdir}
%{__rm} -fr %{buildroot}%{_prefix}/include/

%files
%license LICENSE
%{_bindir}/fluent-bit
%dir %{_sysconfdir}/fluent-bit
%config(noreplace) %{_sysconfdir}/fluent-bit/fluent-bit.conf
%{_sysconfdir}/fluent-bit/parsers.conf
%{_sysconfdir}/fluent-bit/plugins.conf
%{_sysconfdir}/fluent-bit/parsers_ambassador.conf
%{_sysconfdir}/fluent-bit/parsers_cinder.conf
%{_sysconfdir}/fluent-bit/parsers_extra.conf
%{_sysconfdir}/fluent-bit/parsers_java.conf
%{_sysconfdir}/fluent-bit/parsers_openstack.conf
%{_sysconfdir}/fluent-bit/parsers_mult.conf
%{_sysconfdir}/fluent-bit/parsers_multiline.conf

%attr(644, root, root) %{_unitdir}/fluent-bit.service

%pre
%service_add_pre fluent-bit.service
exit 0

%post
%service_add_post fluent-bit.service

%preun
%service_del_preun fluent-bit.service

%postun
%service_del_postun fluent-bit.service

%changelog
