Name:           ros-indigo-h4r-thermapp-camera
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS h4r_thermapp_camera package

Group:          Development/Libraries
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  libusbx-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
The thermapp_camera package provides a library and a node for the Opgal®
ThermApp® Android Thermal Camera

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu May 28 2015 Christian Holl <cyborgx1@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Tue May 26 2015 Christian Holl <cyborgx1@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

