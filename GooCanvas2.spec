%define upstream_name		GooCanvas2
%define upstream_version	0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:	Perl binding for GooCanvas2 widget using Glib::Object::Introspection
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PERLMAX/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(goocanvas-2.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib::Object::Introspection)
BuildRequires:	perl(Gtk3)
BuildRequires:	perl-devel

%{?perl_default_filter}

# libgoocanvas2 typelib loaded by Glib::Object::Introspection
Requires:	libgoocanvas2 >= 2.0

# Provide some class identifiers that are required by other RPM packages. We
# cannot list them all because they are created at run-time from typelib file
# provided by goocanvas2 package that could change between building and
# running.
Provides:	perl(GooCanvas2::Canvas) = %{version}

%description
GooCanvas2 is a new canvas widget for use with Gtk3 that uses
the Cairo 2d library for drawing. This is a simple and basic
implementation of this wonderful Canvas widget.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make}


%install
%make_install

%files
%doc Changes README META.yml
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
