
%define	api_version	1.1.107

Summary:	Vulkan API headers and registry
Summary(pl.UTF-8):	Pliki nagłówkowe i rejestr API Vulkan
Name:		Vulkan-Headers
Version:	%{api_version}
Release:	2
License:	Apache v2.0, parts MIT-like
Group:		Development
Source0:	https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{version}/Vulkan-Headers-%{version}.tar.gz
# Source0-md5:	98dd2be8b74dff529085f078863ef407
URL:		https://github.com/KhronosGroup/Vulkan-Headers/
BuildRequires:	cmake >= 2.8.11
Conflicts:	vulkan-devel < 1.1.107
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header files and registry for Vulkan API.

%description -l pl.UTF-8
Pliki nagłówkowe i rejestr API Vulkan.

%prep
%setup -qn Vulkan-Headers-%{version}

%build
install -d build
cd build

# .pc file creation expect CMAKE_INSTALL_LIBDIR to be relative (to CMAKE_INSTALL_PREFIX)
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/vulkan

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_includedir}/vulkan
%{_datadir}/vulkan/registry
