from io import BytesIO

from translate.storage import txt

from . import test_monolingual


class TestTxtUnit(test_monolingual.TestMonolingualUnit):
    UnitClass = txt.TxtUnit


class TestTxtFile(test_monolingual.TestMonolingualStore):
    StoreClass = txt.TxtFile

    def txtparse(self, txtsource, no_segmentation=False):
        """Helper that parses txt source without requiring files."""
        dummyfile = BytesIO(txtsource.encode())
        return self.StoreClass(dummyfile, no_segmentation=no_segmentation)

    def txtregen(self, txtsource, no_segmentation=False):
        """Helper that converts txt source to txtfile object and back."""
        return bytes(self.txtparse(txtsource, no_segmentation)).decode("utf-8")

    def test_simpleblock(self):
        """Checks that a simple txt block is parsed correctly."""
        txtsource = "bananas for sale"
        txtfile = self.txtparse(txtsource)
        assert len(txtfile.units) == 1
        assert txtfile.units[0].source == txtsource
        assert self.txtregen(txtsource) == txtsource

    def test_multipleblocks(self):
        """Check that multiple blocks are parsed correctly."""
        txtsource = """One\nOne\n\nTwo\n---\n\nThree"""
        txtfile = self.txtparse(txtsource)
        assert len(txtfile.units) == 3
        print(txtsource)
        print(bytes(txtfile))
        print(f"*{txtfile.units[0]}*")
        assert bytes(txtfile).decode("utf-8") == txtsource
        assert self.txtregen(txtsource) == txtsource

    def test_no_segmentation(self):
        """Checks that a simple txt block is parsed correctly."""
        input_string = """
First paragraph

Second paragraph
"""
        expected_output = input_string
        target_store = self.txtparse(input_string, no_segmentation=True)
        assert len(target_store.units) == 1
        assert target_store.units[0].source == expected_output
        output = self.txtregen(input_string, no_segmentation=True)
        assert output == expected_output
