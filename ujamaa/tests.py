from django.test import TestCase

# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
    self.jiji = Profile(image='http//')
  def test_instance(self):
    self.assertTrue(isinstance(self.jiji,Profile))
    
    
 class NeighbourhoodTestClass(TestCase):
  def setUp(self):
    self.hood = Neighbourhood (neighbourhood_image='http',title='hey', description='hello',)
  def test_instance(self):
    self.assertTrue(isinstance(self.hood,Project))
  
  
