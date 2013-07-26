%define upstream_name    Test-Spec
%define upstream_version 0.46

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.46
Release:	1

Summary:	RSpec-like testing for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Spec-0.46.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(TAP::Parser)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Trap)
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl(constant)
BuildArch:	noarch

%description
This is a declarative specification-style testing system for
behavior-driven development (BDD) in Perl. The tests (a.k.a. examples) are
named with strings instead of subroutine names, so your fingers will suffer
less fatigue from underscore-itis, with the side benefit that the test
reports are more legible.

This module is inspired by and borrows heavily from RSpec
(http://rspec.info/documentation/), a BDD tool for the Ruby programming
language.

EXPORTS
    When given *no list* (i.e. 'use Test::Spec;'), this class will export:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-1mdv2011
+ Revision: 690329
- update to new version 0.38

* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.350.0-1
+ Revision: 688483
- import perl-Test-Spec


