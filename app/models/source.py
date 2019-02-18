class Source:
  '''
  Source class to define source objects
  '''

  all_sources=[]
  def __init__(self,id,name):
     self.id=id
     self.name=name

  @classmethod
  def get_sources(cls):
      response=[]

      for source in cls.all_sources:
          response.append(source)

      return response