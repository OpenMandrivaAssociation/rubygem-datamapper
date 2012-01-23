# Generated from datamapper-1.2.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	datamapper

Summary:	An Object/Relational Mapper for Ruby
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://datamapper.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Faster, Better, Simpler.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
