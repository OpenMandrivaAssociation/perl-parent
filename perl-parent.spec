%define upstream_name    parent
%define upstream_version 0.225

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Establish an ISA relationship with base classes at compile time
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

BuildArch:	noarch

Provides:	perl(parent)

%description
Allows you to both load one or more modules, while setting up inheritance from
those modules at the same time.  Mostly similar in effect to

    package Baz;
    BEGIN {
        require Foo;
        require Bar;
        push @ISA, qw(Foo Bar);
    }

By default, every base class needs to live in a file of its own.
If you want to have a subclass and its parent class in the same file, you
can tell C<parent> not to load any modules by using the C<-norequire> switch:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/parent.pm

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.225.0-3mdv2012.0
+ Revision: 765586
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.225.0-2
+ Revision: 764096
- rebuilt for perl-5.14.x

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.225.0-1
+ Revision: 686645
- update to new version 0.225

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.224.0-2
+ Revision: 667471
- mass rebuild

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.224.0-1mdv2011.0
+ Revision: 596724
- update to 0.224

* Thu Sep 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.223.0-1mdv2010.0
+ Revision: 427899
- update to 0.223

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.222.0-1mdv2010.0
+ Revision: 422898
- update to 0.222

* Sun Apr 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.221-3mdv2009.1
+ Revision: 364122
- forgot to bump mkrel

* Sun Apr 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.221-2mdv2009.1
+ Revision: 364121
- adding missing provides

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.221-2mdv2009.0
+ Revision: 268913
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.221-1mdv2009.0
+ Revision: 195404
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 16 2007 Olivier Thauvin <nanardon@mandriva.org> 0.219-1mdv2008.1
+ Revision: 109067
- import perl-parent


