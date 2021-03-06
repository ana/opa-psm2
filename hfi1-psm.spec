#
#  This file is provided under a dual BSD/GPLv2 license.  When using or
#  redistributing this file, you may do so under either license.
#
#  GPL LICENSE SUMMARY
#
#  Copyright(c) 2015 Intel Corporation.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of version 2 of the GNU General Public License as
#  published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  Contact Information:
#  Intel Corporation, www.intel.com
#
#  BSD LICENSE
#
#  Copyright(c) 2015 Intel Corporation.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in
#      the documentation and/or other materials provided with the
#      distribution.
#    * Neither the name of Intel Corporation nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2014-2015 Intel Corporation. All rights reserved.
#
Summary: Intel PSM Libraries
Name: hfi1-psm
Version: 0.7
Release: 238
License: GPLv2
Group: System Environment/Libraries
URL: http://www.intel.com/
Source0: %{name}-%{version}-%{release}.tar.gz
Prefix: /usr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
ExclusiveArch: x86_64
%if 0%{?rhel}%{?rhl}%{?fedora}
Requires: libuuid
%else
Requires: libuuid1
%endif
BuildRequires: libuuid-devel
Conflicts: opa-libs
Obsoletes: hfi-psm
Obsoletes: hfi-psm-debuginfo

%package devel
Summary: Development files for Intel PSM
Group: System Environment/Development
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: libuuid-devel
Conflicts: opa-devel
Obsoletes: hfi-psm-devel

%package compat
Summary: Development files for Intel PSM
Group: System Environment/Development
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Obsoletes: hfi-psm-compat

%description
The PSM Messaging API, or PSM API, is the low-level
user-level communications interface for the Intel(R) OPA
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%description devel
Development files for the libpsm2 library

%description compat
Support for MPIs linked with PSM versions < 2

%prep
%setup -q -n hfi1-psm-%{version}-%{release}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/lib64/libpsm2.so.2.1
/usr/lib64/libpsm2.so.2
/usr/lib/udev/rules.d/40-psm.rules

%files devel
%defattr(-,root,root,-)
/usr/lib64/libpsm2.so
/usr/include/psm2.h
/usr/include/psm2_mq.h
/usr/include/psm2_am.h
# The following files were part of the devel-noship and moved to devel:
/usr/include/hfi1diag/ptl_ips/ipserror.h
/usr/include/hfi1diag/linux-x86_64/bit_ops.h
/usr/include/hfi1diag/linux-x86_64/sysdep.h
/usr/include/hfi1diag/opa_udebug.h
/usr/include/hfi1diag/opa_debug.h
/usr/include/hfi1diag/opa_intf.h
/usr/include/hfi1diag/opa_user.h
/usr/include/hfi1diag/opa_service.h
/usr/include/hfi1diag/opa_common.h
/usr/include/hfi1diag/opa_byteorder.h
/usr/include/hfi1diag/hfi1_deprecated.h

%files compat
%defattr(-,root,root,-)
/usr/lib64/psm2-compat/libpsm_infinipath.so.1
/usr/lib/udev/rules.d/40-psm-compat.rules
/etc/modprobe.d/hfi1-psm-compat.conf
/usr/sbin/hfi1-psm-compat.cmds

%changelog
* Tue Apr 05 2016 -0700-
- Upstream PSM2 source code for Fedora.

