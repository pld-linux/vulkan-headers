Summary:	Vulkan API headers and registry
Summary(pl.UTF-8):	Pliki nagłówkowe i rejestr API Vulkan
Name:		Vulkan-Headers
# note: prefer "sdk-" tags for better quality level
Version:	1.3.243.0
Release:	1
License:	Apache v2.0, parts MIT-like
Group:		Development
#Source0Download: https://github.com/KhronosGroup/Vulkan-Headers/tags
Source0:	https://github.com/KhronosGroup/Vulkan-Headers/archive/sdk-%{version}/Vulkan-Headers-sdk-%{version}.tar.gz
# Source0-md5:	848df8eb68f8f79a2b5b39aecc0595c4
URL:		https://github.com/KhronosGroup/Vulkan-Headers/
BuildRequires:	cmake >= 3.15
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	libxcb-devel
Requires:	wayland-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXrandr-devel
Conflicts:	vulkan-devel < 1.1.107
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header files and registry for Vulkan API.

%description -l pl.UTF-8
Pliki nagłówkowe i rejestr API Vulkan.

%prep
%setup -qn Vulkan-Headers-sdk-%{version}

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_includedir}/vk_video
%{_includedir}/vulkan
%{_datadir}/vulkan/registry
%{_datadir}/cmake/VulkanHeaders
