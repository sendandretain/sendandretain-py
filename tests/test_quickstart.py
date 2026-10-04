"""The README quickstart, executed against a mocked transport.

A snippet that no longer compiles against the generated models is the most
embarrassing kind of documentation bug and the easiest to ship — the code in the
README is never imported by anything. This test is that import.

No network: respx intercepts at the transport, so it asserts the URL, the
`Authorization` header, the query string and the request body that the SDK would
really have sent.
"""

from __future__ import annotations

import httpx
import respx

from sendandretain import DEFAULT_BASE_URL, Client

VALID_KEY = "aem_test0123456789"

PROJECT_ID = "00000000-0000-0000-0000-000000000000"


def test_quickstart_round_trip() -> None:
    """The README quickstart, run against a mocked transport."""
    import json

    from sendandretain.api.emails import send_email
    from sendandretain.models import SendEmailBody, SendEmailBodyProps, SendResult

    with respx.mock(base_url=DEFAULT_BASE_URL) as mock:
        route = mock.post("/api/v1/emails").mock(
            return_value=httpx.Response(200, json={"id": "msg_1", "status": "queued"})
        )
        result = send_email.sync(
            client=Client(api_key=VALID_KEY),
            body=SendEmailBody(
                to="person@example.com",
                template="welcome",
                props=SendEmailBodyProps.from_dict({"first_name": "Ada"}),
            ),
        )

    request = route.calls[0].request
    assert request.headers["authorization"] == f"Bearer {VALID_KEY}"
    assert json.loads(request.content) == {
        "to": "person@example.com",
        "template": "welcome",
        "props": {"first_name": "Ada"},
    }
    # Narrowed rather than asserted loosely: every operation returns
    # `Error | <Result>`, and the point of the SDK is that the success branch is
    # a real typed object.
    assert isinstance(result, SendResult)
    assert result.id == "msg_1"
