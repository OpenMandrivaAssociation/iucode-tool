Name: iucode-tool
Version: 2.3.1
Release: 1
Source0: https://gitlab.com/iucode-tool/releases/raw/latest/%{name}_%{version}.tar.xz
Summary: Tool for working with Intel microcode updates
URL: https://gitlab.com/iucode-tool/iucode-tool/wikis/home
License: GPLv2+
Group: System/Kernel and hardware
ExclusiveArch: %{ix86} x86_64
Obsoletes: microcode_ctl
Suggests: microcode-intel

%description
Tool for working with Intel microcode updates

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std

%files
%{_sbindir}/*
%{_mandir}/*/*
