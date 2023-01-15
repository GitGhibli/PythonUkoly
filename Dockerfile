FROM python

WORKDIR .

COPY test_all_submissions.py ./
COPY /assignments ./assignments

CMD [ "python", "./test_all_submissions.py", "asterisk_triangles" ]