from ghl_n8n_leads.src.app import run_flow


def test_fieldroutes_flow_has_steps():
    flow = run_flow("fieldroutes")
    assert len(flow) == 5
    assert flow[0]["step"] == "Receive FieldRoutes request"


def test_callgear_flow_has_steps():
    flow = run_flow("callgear")
    assert any("CallGear" in step["step"] for step in flow)


def test_callrail_flow_has_steps():
    flow = run_flow("callrail")
    assert any("CallRail" in step["step"] for step in flow)


def test_meta_flow_includes_all_sources():
    flow = run_flow("meta")
    assert any("Ingest FieldRoutes source" in step["step"] for step in flow)
    assert any("Ingest CallGear source" in step["step"] for step in flow)
    assert any("Ingest CallRail source" in step["step"] for step in flow)
