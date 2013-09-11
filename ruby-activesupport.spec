%define pkgname activesupport
Summary:	Utility libraries for Ruby on Rails
Name:		ruby-%{pkgname}
Version:	3.0.3
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	474ab3e5963afdad6a9c6c66ff08b16d
URL:		http://rubyforge.org/projects/activesupport/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-builder >= 2.1.2
Requires:	ruby-i18n
Requires:	ruby-json
Requires:	ruby-memcache-client
Requires:	ruby-mocha >= 0.9.7
Requires:	ruby-nokogiri >= 1.1.1
Requires:	ruby-tzinfo
Provides:	ruby-ActiveSupport
Obsoletes:	ruby-ActiveSupport
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility libraries for Ruby on Rails.

%description -l pl.UTF-8
Biblioteki narzędziowe dla Ruby on Rails.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

# JRuby crap
rm lib/active_support/xml_mini/jdom.rb

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri
rm -r ri/{Class,Date,DateTime} \
	ri/{Enumerable,FalseClass,File,Float,Hash} \
	ri/{Integer,Kernel,Logger} \
	ri/{Module,NameError,NilClass,Numeric} \
	ri/{Object,Range,Regexp,String} \
	ri/{Symbol,Test,Time,TrueClass,Process,Array,BigDecimal} \
	ri/{Benchmark,ERB,Fixnum,I18n,LoadError}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{ruby_vendorlibdir}/active_support
%{ruby_vendorlibdir}/active_support.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/ActiveSupport
