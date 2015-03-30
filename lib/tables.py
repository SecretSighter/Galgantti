class Table(list):
	# subclasses should override the headings variable
	headings = [ 'Column 1', 'Column 2' ]
	# the number of rows to show on a page
	rows_per_page = 5
	# the url to request tables pages from
	endpoint = '/app/view.table/pagenum/'

	def paginate(self, request, qry):
		try:
			page = int(request.REQUEST.get('table_page'))
		except ValueError, TypeError:
			page = 0
		qry = qry[page * self.rows_per_page: (page + 1) * self.rows_per_page]
		return qry

	def __init__(self, request, *args, **kwargs):
		super(Table, self).__init__(*args, **kwargs)
		self.request = request
		self.webid = request.generate_webid.yield_next()

	def __str__(self):
		# output the table html here
		html = [];
		html.append('<table class="table table-bordered table-striped table-hover">')
		html.append('<tr>')
		for row in self.headings:
			html.append('<th>')
			html.append(row)
			html.append('</th>')
		html.append('</tr>')
		for row in self:
			# output each row
			html.append('<tr>')
			for cell in row:
				html.append('<td>')
				html.append(cell)
				html.append('</td>')	
			html.append('</tr>')
		html.append("</table>")
		html.append('<nav>	<ul class="pagination"><li><a href="#" aria-label="Previous" class="previous_page_button"><span aria-hidden="true">&laquo;</span></a></li><li><a href="#">1</a></li><li><a href="#">2</a></li><li><a href="#">3</a></li><li><a href="#">4</a></li><li><a href="#">5</a></li><li><a href="#" aria-label="Next" class="next_page_button"><span aria-hidden="true">&raquo;</span></a></li></ul></nav>')
		return ''.join(html)
		
class MyTable(Table):
	headings = [ 'Name', 'Salary' ]
	endpoint = '/app/view.table/pagenum/'	