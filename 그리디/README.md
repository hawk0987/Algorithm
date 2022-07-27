<div class="row">
		<div class="col-md-12">
			<div id="result_log"></div>
		</div>
		<div class="col-md-12">
							<ul class="nav nav-pills no-print problem-menu"><li class="active">
	<a href="/problem/1931">1931번</a>
</li><li><a href="/submit/1931">제출</a></li><li><a href="/problem/status/1931">맞힌 사람</a></li><li><a href="/short/status/1931">숏코딩</a></li><li><a href="/problem/history/1931">재채점 결과</a></li><li><a href="/status?from_problem=1&amp;problem_id=1931">채점 현황</a></li><li><a href="/status?from_mine=1&amp;problem_id=1931&amp;user_id=hawk0987">내 제출</a></li><li><a href="https://solved.ac/contribute/1931" target="_blank"><i class="fa fa-external-link"></i> 난이도 기여</a></li><li class="dropdown"><a class="dropdown-toggle" id="drop5" role="button" data-toggle="dropdown" href="#">강의<b class="caret"></b></a><ul id="menu2" class="dropdown-menu" role="menu" aria-labelledby="drop5"><li><a tabindex="-1" href="https://code.plus/course/43">알고리즘 중급 1/3</a></li></ul></li><li><a href="/board/search/all/problem/1931">질문 검색</a></li></ul>
					</div>
		<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">
	1931번
 - </span><span id="problem_title">회의실 배정</span>
				<span class="problem-label problem-label-ac">성공</span>				<div class="btn-group pull-right problem-button">
																										<button class="btn btn-default" type="button" id="favorite_button" data-favorite="0"><span class="glyphicon glyphicon-star-empty" id="favorite_image"></span></button>
																																						</div>
				</h1>
									
							</div>
		</div>
		<div class="col-md-12"><div class="table-responsive"><table class="table" id="problem-info"><thead><tr><th style="width:16%;">시간 제한</th><th style="width:16%;">메모리 제한</th><th style="width:17%;">제출</th><th style="width:17%;">정답</th><th style="width:17%;">맞힌 사람</th><th style="width:17%;">정답 비율</th></tr></thead><tbody><tr><td>2 초 </td><td>128 MB</td><td>131091</td><td>40622</td><td>28907</td><td>29.492%</td></tr></tbody></table></div></div>
						<div id="problem-body" class="">
			<div class="col-md-12">
				<section id="description" class="problem-section">
				<div class="headline">
				<h2>문제</h2>
				</div>
				<div id="problem_description" class="problem-text">
				<p>한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.</p>

				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 2<sup>31</sup>-1보다 작거나 같은 자연수 또는 0이다.</p>

					</div>
					</section>
				</div>
	
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.</p>

					</div>
					</section>
				</div>
						<div class="col-md-12">
			<section id="limit" style="display:none;" class="problem-section">
			<div class="headline">
			<h2>제한</h2>
			</div>
			<div id="problem_limit" class="problem-text">
						</div>
			</section>
			</div>
																	<div class="col-md-12">
				<div class="row">
					<div class="col-md-6">
						<section id="sampleinput1">
						<div class="headline">
						<h2>예제 입력 1
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-1">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-1">11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput1">
						<div class="headline">
						<h2>예제 출력 1
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-1">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-1">4
</pre>
						</section>
					</div>
									</div>
				</div>
										<div class="col-md-12">
				<section id="hint" class="problem-section">
				<div class="headline">
				<h2>힌트</h2>
				</div>
				<div id="problem_hint" class="problem-text">
				<p>(1,4), (5,7), (8,11), (12,14) 를 이용할 수 있다.</p>

				</div>
				</section>
			</div>
								</div>
									<div class="col-md-12"><section id="source"><div class="headline"><h2>출처</h2></div><ul><li>빠진 조건을 찾은 사람:&nbsp;<a href="/user/andy627">andy627</a></li><li>데이터를 추가한 사람:&nbsp;<a href="/user/jws0324">jws0324</a>, <a href="/user/kimchangyoung">kimchangyoung</a>, <a href="/user/rosedskim">rosedskim</a></li></ul></section></div>
													<div class="col-md-12">
					<section id="problem_tags">
					<div class="headline">
					<h2>알고리즘 분류</h2>
					</div>
																																												  <ul class="spoiler-list">
  						  							<li>
  							<a href="/problem/tag/33" class="spoiler-link">그리디 알고리즘</a>
  							</li>
  						  							<li>
  							<a href="/problem/tag/97" class="spoiler-link">정렬</a>
  							</li>
  						  					</ul>
										</section>
				</div>
																						<div class="col-md-12">
					<section id="problem_memo">
					<div class="headline">
					<h2>메모</h2>
					</div>
						<div id="problem-memo-view" class="problem-text">
			</div>
	<div id="problem-memo-edit" style="display: none;"><textarea name="memo-content" id="memo-content" class="form-control" style="display:none;"></textarea><div class="editor-toolbar"><a title="Bold (Ctrl-B)" tabindex="-1" class="fa fa-bold"></a><a title="Italic (Ctrl-I)" tabindex="-1" class="fa fa-italic"></a><a title="Heading (Ctrl-H)" tabindex="-1" class="fa fa-header"></a><a title="Big Heading" tabindex="-1" class="fa fa-header fa-header-x fa-header-1"></a><a title="Medium Heading" tabindex="-1" class="fa fa-header fa-header-x fa-header-2"></a><a title="Small Heading" tabindex="-1" class="fa fa-header fa-header-x fa-header-3"></a><i class="separator">|</i><a title="Code (Ctrl-Alt-C)" tabindex="-1" class="fa fa-code"></a><a title="Quote (Ctrl-')" tabindex="-1" class="fa fa-quote-left"></a><a title="Generic List (Ctrl-L)" tabindex="-1" class="fa fa-list-ul"></a><a title="Numbered List (Ctrl-Alt-L)" tabindex="-1" class="fa fa-list-ol"></a><a title="Insert Horizontal Line" tabindex="-1" class="fa fa-minus"></a><i class="separator">|</i><a title="Create Link (Ctrl-K)" tabindex="-1" class="fa fa-link"></a><a title="Insert Image (Ctrl-Alt-I)" tabindex="-1" class="fa fa-picture-o"></a><i class="separator">|</i><a title="Toggle Preview (Ctrl-P)" tabindex="-1" class="fa fa-eye no-disable"></a><a title="Toggle Side by Side (F9)" tabindex="-1" class="fa fa-columns no-disable no-mobile"></a><a title="Toggle Fullscreen (F11)" tabindex="-1" class="fa fa-arrows-alt no-disable no-mobile"></a></div><div class="CodeMirror cm-s-paper CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px;"><div style="position: relative;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"></div><div class="CodeMirror-code"></div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px;"></div><div class="CodeMirror-gutters" style="display: none;"></div></div></div><div class="editor-preview-side"></div><div class="editor-statusbar"><span class="autosave"></span><span class="lines">1</span><span class="words">0</span><span class="cursor">0:0</span></div></div><p class="lead text-center no-print" id="problem-memo-button"><a href="#" class="problem-memo-write">메모 작성하기</a></p><p class="lead text-center no-print" id="problem-memo-save-div" style="display: none;"><button type="button" class="btn btn-primary btn-lg" id="problem-memo-save" data-loading-text="작성 중...">저장</button>&nbsp;<button type="button" class="btn btn-lg" id="problem-memo-cancel">취소</button></p>

					</section>
				</div>
						</div>
