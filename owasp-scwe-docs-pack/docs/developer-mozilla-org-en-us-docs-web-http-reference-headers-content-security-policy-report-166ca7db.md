---
title: "Content-Security-Policy: report-to directive"
source_url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to"
host: "developer.mozilla.org"
depth: 2
selector: "body"
fetched_at: "2026-10-24T02:29:46.339Z"
---
-   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#content)
-   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#mdn-search)

# Content-Security-Policy: report-to directive

Baseline 2026

Newly available

Since March 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

-   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#browser_compatibility)
-   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)

The `Content-Security-Policy` **`report-to`** directive indicates the name of the endpoint that the browser should use for reporting CSP violations.

If a CSP violation occurs, a report is generated that contains a serialized [`CSPViolationReport`](https://developer.mozilla.org/en-US/docs/Web/API/CSPViolationReport) object instance. This report is sent to the URL that corresponds to the endpoint name, using the generic mechanisms defined in the [Reporting API](https://developer.mozilla.org/en-US/docs/Web/API/Reporting_API).

The server must separately provide the mapping between endpoint names and their corresponding URLs in the [`Reporting-Endpoints`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints) HTTP response header.

<table class="properties"><tbody><tr><th scope="row">CSP version</th><td>3</td></tr><tr><th scope="row">Directive type</th><td><a href="https://developer.mozilla.org/en-US/docs/Glossary/Reporting_directive">Reporting directive</a></td></tr><tr><th colspan="2" scope="row">This directive is not supported in the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta"><code>&lt;meta&gt;</code></a> element.</th></tr></tbody></table>

## [Syntax](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#syntax)

http

```
Content-Security-Policy: …; report-to <endpoint_name>
```

`<endpoint_name>` is the name of an endpoint provided by the [`Reporting-Endpoints`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints) HTTP response header. It can also be the name of a group that is provided by the server in the [`Report-To`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Report-To) HTTP response header.

### [Violation report syntax](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#violation_report_syntax)

A CSP violation report is a JSON-serialized [`CSPViolationReport`](https://developer.mozilla.org/en-US/docs/Web/API/CSPViolationReport) object, with a `type` property that has a value of `"csp-violation"`. Reports are sent to the target endpoint(s) via a [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST) operation with a [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) of `application/reports+json`.

The JSON for a single report might look like this:

json

```
{
  "age": 53531,
  "body": {
    "blockedURL": "inline",
    "columnNumber": 39,
    "disposition": "enforce",
    "documentURL": "https://example.com/csp-report",
    "effectiveDirective": "script-src-elem",
    "lineNumber": 121,
    "originalPolicy": "default-src 'self'; report-to csp-endpoint-name",
    "referrer": "https://www.google.com/",
    "sample": "console.log(\"lo\")",
    "sourceFile": "https://example.com/csp-report",
    "statusCode": 200
  },
  "type": "csp-violation",
  "url": "https://example.com/csp-report",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
```

## [Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#usage_notes)

The `report-to` directive is intended to replace `report-uri`, and browsers that support `report-to` ignore the `report-uri` directive. However, until `report-to` is broadly supported you can specify both directives as shown:

http

```
Content-Security-Policy: …; report-uri https://endpoint.example.com; report-to endpoint_name
```

Note that other examples in this topic do not show `report-uri`.

## [Examples](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#examples)

### [Setting a CSP violation report endpoint](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#setting_a_csp_violation_report_endpoint)

A server can define the mapping between endpoint names and URLs using the [`Reporting-Endpoints`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints) header in the HTTP response. Any name can be used: here we've chosen `name-of-endpoint`.

http

```
Reporting-Endpoints: name-of-endpoint="https://example.com/csp-reports"
```

The server can set this endpoint name as the target for sending CSP violation reports to using the `report-to` directive:

http

```
Content-Security-Policy: default-src 'self'; report-to name-of-endpoint
```

## [Specifications](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#specifications)

| Specification |
| --- |
| [Content Security Policy Level 3
\# directive-report-to](https://w3c.github.io/webappsec-csp/#directive-report-to) |

## [Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#browser_compatibility)

## [See also](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to#see_also)

-   [`Reporting-Endpoints`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Reporting-Endpoints)
-   [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
-   [`Content-Security-Policy-Report-Only`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only)
-   [Reporting API](https://developer.mozilla.org/en-US/docs/Web/API/Reporting_API)

## Help improve MDN

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Mar 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/report-to/contributors.txt).

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/http/reference/headers/content-security-policy/report-to/index.md?plain=1 "Folder: en-us/web/http/reference/headers/content-security-policy/report-to (Opens in a new tab)") • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FReference%2FHeaders%2FContent-Security-Policy%2Freport-to&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhttp%2Freference%2Fheaders%2Fcontent-security-policy%2Freport-to%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FReference%2FHeaders%2FContent-Security-Policy%2Freport-to%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhttp%2Freference%2Fheaders%2Fcontent-security-policy%2Freport-to%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6720d579bd658f02c56363805e97e69f93dc79f1%0A*+Document+last+modified%3A+2026-03-22T23%3A36%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
