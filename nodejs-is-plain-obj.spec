%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# ava is not in fedora yet
%global enable_tests 0
%global module_name is-plain-obj
%global commit0 ca2adca4deadaa0a632d8abc40e1e4654ccd4c1b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.0.0
Release:        3%{?dist}
Summary:        Check if a value is a plain object

License:        MIT
URL:            https://github.com/sindresorhus/is-plain-obj
Source0:        https://github.com/sindresorhus/%{module_name}/archive/%{commit0}.tar.gz#/%{module_name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(ava)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{commit0}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -p package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Enable scl macros, fix license macro for el6

* Fri Jul 31 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging