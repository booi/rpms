# $Id$

# The source contains only binaries...
%define _use_internal_dependency_generator 0
# Disable stripping or the default.sfx will get trashed
%define __strip /bin/true

Summary: RAR archiver to manage RAR archive files.
Name: rar
Version: 3.3.0
Release: 1.fr
License: Shareware
Group: Applications/Archiving
Source: http://www.rarlabs.com/rar/rarlinux-%{version}.tar.gz
URL: http://www.rarlabs.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: i586

%description
RAR is a powerful tool allowing you to manage and control archive files.
Console RAR supports archives only in RAR format, which names usually have
a ".rar" extension. ZIP and other formats are not supported.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
install -m 755 -D rar %{buildroot}%{_bindir}/rar
install -m 644 -D rarfiles.lst %{buildroot}%{_sysconfig}/rarfiles.lst
install -m 755 -D default.sfx %{buildroot}%{_libdir}/default.sfx

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc file_id.diz *.txt
%{_bindir}/rar
%{_libdir}/default.sfx

%changelog
* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 3.3.0-1.fr
- Update to 3.3.0.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 3.2.0-3.fr
- Rebuild for Fedora Core 1.

* Mon Nov  3 2003 Matthias Saou <http://freshrpms.net/> 3.2.0-2.fr
- Disable stripping to not trash the default.sfx file.
- Add back rarfiles.lst, as it does work, thanks to Ondrej Svejda.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 3.2.0-1.fr
- Update to latest version.
- Spec file cleanup.
- Remove the internal dep check to avoid "corrupted program header size" msg.

* Sun Mar 18 2001 Matthias Saou <http://freshrpms.net/>
- Fix the %files with a %dir (cleaner uninstall)
- Spec file cleanup

* Sun Mar 18 2001 Alexander Skwar <ASkwar@Linux-Mandrake.com> 2.80-1
- New non-beta release

* Mon Feb 26 2001 Alexander Skwar <ASkwar@Linux-Mandrake.com> 2.80b5-1
- New release, see http://www.rarsoft.com/rar/WhatsNew.txt for
  list of fixed bugs

* Sun Jan 28 2001 Alexander Skwar <ASkwar@Linux-Mandrake.com> 2.80b4-1
- Nothing exciting, besides the latest beta

* Thu Jan  4 2001 Alexander Skwar <ASkwar@Linux-Mandrake.com> 2.80b2-1
- Another new version

* Sat Sep 15 2000 01:00:35 Alexander Skwar <ASkwar@DigitalProjects.com> 2.71-1
- New version
