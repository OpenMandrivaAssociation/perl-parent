%define upstream_name    parent
%define upstream_version 0.223

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Establish an ISA relationship with base classes at compile time
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Provides: perl(parent)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/parent.pm
