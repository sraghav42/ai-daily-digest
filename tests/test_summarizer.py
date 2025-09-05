from news.summarizer import summarize_text

def test_summarize_text_success(monkeypatch):
    class FakeResponse:
        text = "• Point 1\n• Point 2"
    monkeypatch.setattr("news.summarizer.model.generate_content", lambda prompt: FakeResponse())

    result = summarize_text("Some long article text")
    assert "Point 1" in result

def test_summarize_text_failure(monkeypatch):
    def fake_generate_content(prompt):
        raise Exception("Fake error")
    monkeypatch.setattr("news.summarizer.model.generate_content", fake_generate_content)

    result = summarize_text("Some long article text")
    assert "[Error summarizing text:" in result