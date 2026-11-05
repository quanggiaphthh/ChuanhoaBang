"""Font-face metadata gates prevent measuring with the wrong Times New Roman face."""
import pytest
from PIL import ImageFont, features

from chuanhoabang import TableError, core


class _Face:
    def __init__(self, family, style):
        self.identity = (family, style)

    def getname(self):
        return self.identity


def _install_faces(monkeypatch, *faces):
    iterator = iter(faces)
    monkeypatch.setattr(features, "check", lambda _name: True)
    monkeypatch.setattr(ImageFont, "truetype", lambda *_args, **_kwargs: next(iterator))


@pytest.mark.parametrize("style", ["Bold", "Italic", "Bold Italic"])
def test_regular_font_slot_rejects_bold_or_italic_face(monkeypatch, style):
    _install_faces(monkeypatch, _Face("Times New Roman", style))

    with pytest.raises(TableError, match="TNR_REGULAR_FACE_REQUIRED"):
        core._load_fonts("regular.ttf", None)


@pytest.mark.parametrize("style", ["Regular", "Italic", "Bold Italic"])
def test_bold_font_slot_requires_nonitalic_bold_face(monkeypatch, style):
    _install_faces(monkeypatch, _Face("Times New Roman", "Regular"),
                   _Face("Times New Roman", style))

    with pytest.raises(TableError, match="TNR_BOLD_FACE_REQUIRED"):
        core._load_fonts("regular.ttf", "bold.ttf")
