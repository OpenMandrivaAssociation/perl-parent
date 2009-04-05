%define module   parent
%define version    0.221
%define release    %mkrel 3

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Establish an ISA relationship with base classes at compile time
Url:        http://search.cpan.org/dist/%{module}
Source:     http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{module}-%{version}.tar.gz
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

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
