FROM python

WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .

ENV DB_URL=mysql://admin:Navya_56@database-2.cacjlsbfaqdn.ap-south-1.rds.amazonaws.com/aws
ENV ACCESS_KEY=AKIA6EHEVZYHMAOG5UXJ
ENV SECRET_KEY=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
#this runs when image is built
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ,"app.py" ] 
