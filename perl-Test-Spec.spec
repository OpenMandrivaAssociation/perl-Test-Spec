%define upstream_name    Test-Spec
%define upstream_version 0.38

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    RSpec-like testing for Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(List::Util)
BuildRequires: perl(Package::Stash)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(TAP::Parser)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(Tie::IxHash)
BuildRequires: perl(constant)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


