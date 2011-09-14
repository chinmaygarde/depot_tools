from tests.patches_data import GIT, RAW
    p = patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, [])
    self._check_patch(p, 'chrome/file.cc', RAW.PATCH)
    p = patch.FilePatchDiff('git_cl/git-cl', GIT.MODE_EXE, [])
        p, 'git_cl/git-cl', GIT.MODE_EXE, is_git_diff=True, patchlevel=1,
    p = patch.FilePatchDiff('git_cl/git-cl', GIT.MODE_EXE_JUNK, [])
        p, 'git_cl/git-cl', GIT.MODE_EXE_JUNK, is_git_diff=True, patchlevel=1,
    p = patch.FilePatchDiff('foo', RAW.NEW, [])
    self._check_patch(p, 'foo', RAW.NEW, is_new=True)
    p = patch.FilePatchDiff('foo', GIT.NEW, [])
        p, 'foo', GIT.NEW, is_new=True, is_git_diff=True, patchlevel=1)
    p = patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, [])
    lines = RAW.PATCH.splitlines(True)
    self.assertEquals(RAW.PATCH, p.get())
    p = patch.FilePatchDiff('chrome/file.cc', RAW.MINIMAL_NEW, [])
    self.assertEquals(RAW.MINIMAL_NEW, p.diff_header)
    self.assertEquals(RAW.MINIMAL_NEW, p.get())
    p = patch.FilePatchDiff('chrome/file.cc', RAW.MINIMAL_DELETE, [])
    self.assertEquals(RAW.MINIMAL_DELETE, p.diff_header)
    self.assertEquals(RAW.MINIMAL_DELETE, p.get())
        patch.FilePatchDiff('chrome/file.cc', RAW.PATCH, []),
            'tools\\clang_check/README.chromium', GIT.DELETE, []),
        patch.FilePatchDiff('tools/run_local_server.sh', GIT.RENAME, []),
            'chromeos\\views/webui_menu_widget.h', GIT.RENAME_PARTIAL, []),
        patch.FilePatchDiff('pp', GIT.COPY, []),
        patch.FilePatchDiff('foo', GIT.NEW, []),
    for line in RAW.PATCH.splitlines(True):
        patch.FilePatchDiff('chrome\\file.cc', RAW.PATCH, []),
    mangled_patch = RAW.PATCH.replace('chrome/', 'chrome\\')
    self.assertEquals(RAW.PATCH, patches.patches[0].get())
    p = patch.FilePatchDiff('tools/clang_check/README.chromium', RAW.DELETE, [])
        p, 'tools/clang_check/README.chromium', RAW.DELETE, is_delete=True)
    p = patch.FilePatchDiff('tools/clang_check/README.chromium', GIT.DELETE, [])
        p, 'tools/clang_check/README.chromium', GIT.DELETE, is_delete=True,
    p = patch.FilePatchDiff('tools/run_local_server.sh', GIT.RENAME, [])
    self._check_patch(p, 'tools/run_local_server.sh', GIT.RENAME,
        'chromeos/views/webui_menu_widget.h', GIT.RENAME_PARTIAL, [])
        p, 'chromeos/views/webui_menu_widget.h', GIT.RENAME_PARTIAL,
    p = patch.FilePatchDiff('pp', GIT.COPY, [])
    self._check_patch(p, 'pp', GIT.COPY, is_git_diff=True, patchlevel=1,
    p = patch.FilePatchDiff('file_a', RAW.MINIMAL, [])
    self._check_patch(p, 'file_a', RAW.MINIMAL)
    p = patch.FilePatchDiff('file_a', RAW.NEW_NOT_NULL, [])
    self._check_patch(p, 'file_a', RAW.NEW_NOT_NULL)
    p = patch.FilePatchDiff('file_b', RAW.MINIMAL_RENAME, [])
    self._check_patch(
        p, 'file_b', RAW.MINIMAL_RENAME, source_filename='file_a', is_new=True)
    p = patch.FilePatchDiff('wtf2', GIT.COPY_PARTIAL, [])
        p, 'wtf2', GIT.COPY_PARTIAL, source_filename='wtf', is_git_diff=True,
        patchlevel=1, is_new=True)

  def testGitNewExe(self):
    p = patch.FilePatchDiff('natsort_test.py', GIT.NEW_EXE, [])
        p, 'natsort_test.py', GIT.NEW_EXE, is_new=True, is_git_diff=True,
        patchlevel=1, svn_properties=[('svn:executable', '*')])
  def testGitNewMode(self):
    p = patch.FilePatchDiff('natsort_test.py', GIT.NEW_MODE, [])
        p, 'natsort_test.py', GIT.NEW_MODE, is_new=True, is_git_diff=True,
        patchlevel=1)
      patch.FilePatchDiff('foo', RAW.PATCH, [])
        patch.FilePatchDiff('chrome\\file.cc', RAW.PATCH, []),