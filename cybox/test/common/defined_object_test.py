import unittest

from cybox.common.defined_object import DefinedObject
from cybox.objects.address_object import Address
from cybox.test import round_trip


class TestDefinedObject(unittest.TestCase):
    
    def test_empty_dict(self):
        self.assertEqual(None, DefinedObject.from_dict({}))

    def test_no_xsi_type(self):
        # d does not have the required 'xsi:type' key.
        d = {'key': 'value'}

        self.assertRaises(ValueError, DefinedObject.from_dict, d)

    def test_detect_address(self):
        d = {'xsi:type': Address._XSI_TYPE}

        self.assertTrue(isinstance(DefinedObject.from_dict(d), DefinedObject))
        self.assertTrue(isinstance(DefinedObject.from_dict(d), Address))


if __name__ == "__main__":
    unittest.main()
