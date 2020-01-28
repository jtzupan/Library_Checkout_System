


tz = User(username='tzupan', common_id=1234, email='tylerzupan@quickenloans.com')
db.session.add(tz)
jw = User(username='jwoz', common_id=2345, email='jwoz@quickenloans.com')
db.session.add(jw)
mo = User(username='moz', common_id=4567, email='moz@quickenloans.com')
db.session.add(mo)
db.session.commit()

b1 = Books(title='Data Science From Scratch'
           , author='Person A'
           , publish_year=2015)
db.session.add(b1)
b2 = Books(title='Deep Learning'
           , author='Person B'
           , publish_year=2016)
db.session.add(b2)
db.session.commit()

description_1 = DescriptionDim(description='Python')
db.session.add(description_1)
description_2 = DescriptionDim(description='Statistics')
db.session.add(description_2)
description_3 = DescriptionDim(description='R')
db.session.add(description_3)
db.session.commit()

bd_1 = BookDescriptionDim(book_id=1, description_id=1)
db.session.add(bd_1)
bd_2 = BookDescriptionDim(book_id=1, description_id=2)
db.session.add(bd_2)
bd_3 = BookDescriptionDim(book_id=2, description_id=2)
db.session.add(bd_3)
bd_4 = BookDescriptionDim(book_id=2, description_id=3)
db.session.add(bd_4)
db.session.commit()