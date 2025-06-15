Name:		cachefilesd
Version:	0.10.10
Release:	1
Source0:	https://people.redhat.com/~dhowells/fscache/cachefilesd-0.10.10.tar.bz2
Summary:	Tools for caching network filesystems
URL:		https://people.redhat.com/~dhowells/fscache
License:	GPL
Group:		System
BuildRequires:	make

%description
The cachefilesd daemon manages the caching files and directories mounted through
network file systems such as NFS, sshfs or AFS, to do persistent caching to
the local disk.

%prep
%autosetup -p1

%conf

%build
%make_build \
	ETCDIR=%{_sysconfdir} \
	SBINDIR=%{_sbindir} \
	MANDIR=%{_mandir} \
	CC="%{__cc}" \
	CFLAGS="%{optflags}"

%install
%make_install \
	ETCDIR=%{_sysconfdir} \
	SBINDIR=%{_sbindir} \
	MANDIR=%{_mandir} \
	CC="%{__cc}" \
	CFLAGS="%{optflags}"

mkdir -p %{buildroot}%{_unitdir}
install -c -m 644 cachefilesd.service %{buildroot}%{_unitdir}/

%files
%config(noreplace) %{_sysconfdir}/cachefilesd.conf
%{_unitdir}/cachefilesd.service
%{_bindir}/cachefilesd
%{_mandir}/man5/cachefilesd.conf.5*
%{_mandir}/man8/cachefilesd.8*
