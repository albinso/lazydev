
from server import Pipeline
import unittest

class TestPipeline(unittest.TestCase):
    def test_smoke(self):
        pipe = Pipeline("tests/test", "tests/testdeploy")
        output, error, code = pipe.run_pipeline()
        self.assertEqual(error, None)
        self.assertEqual(code, 0)

if __name__ == '__main__':
    unittest.main()
