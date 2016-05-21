(add-to-list 'load-path "~/.emacs.d/")
(require 'web-mode)
(add-to-list 'auto-mode-alist '("\\.html\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.jsx\\'" . web-mode))
(add-to-list 'auto-mode-alist '("\\.css\\'" . web-mode))
(setq web-mode-markup-indent-offset 2)
(setq web-mode-css-indent-offset 2)
(setq web-mode-code-indent-offset 2)
(add-hook 'js-mode-hook
          (lambda ()
            (setq indent-tabs-mode nil)
            (setq js-indent-level 2)))

(add-to-list 'auto-mode-alist '("\\.ts$" . js-mode))

(require 'go-mode-load)
;(require 'auto-complete-config)
;(add-to-list 'ac-dictionary-directories "~/.emacs.d/ac-dict")
;(ac-config-default)
;(require 'go-autocomplete)
;(add-hook 'before-save-hook 'gofmt-before-save)
;(add-hook 'go-mode-hook (lambda ()
;                          (local-set-key (kbd "C-c C-r") 'go-remove-unused-imports)))
(setq-default tab-width 4)
(setq-default fill-column 100)
(custom-set-variables
  ;; custom-set-variables was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 '(indent-tabs-mode nil)
 '(inhibit-startup-screen t)
 '(tab-always-indent t)
 '(tab-stop-list (quote (4 8 12 16 20 24 28 32 36 40 44 48 52)))
 '(backup-directory-alist (quote (("." . "~/.emacs-backups")))))
(defun my-go-mode-hook ()
 ; Use goimports instead of go-fmt
 (setq gofmt-command "goimports")
 ; Call Gofmt before saving
 (add-hook 'before-save-hook 'gofmt-before-save)
 ; Customize compile command to run go build
 (if (not (string-match "go" compile-command))
     (set (make-local-variable 'compile-command)
          "go build -v"))
 ; Godef jump key binding
 (local-set-key (kbd "M-.") 'godef-jump)
 (local-set-key (kbd "C-c c") 'compile)
 )
(add-hook 'go-mode-hook 'my-go-mode-hook)

(add-to-list 'load-path "~/.emacs.d/lisp")
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "~/.emacs.d/lisp/ac-dict")
(ac-config-default)

(require 'go-autocomplete)
(require 'auto-complete-config)

(autoload 'markdown-mode "markdown-mode"
   "Major mode for editing Markdown files" t)
(add-to-list 'auto-mode-alist '("\\.text\\'" . markdown-mode))
(add-to-list 'auto-mode-alist '("\\.markdown\\'" . markdown-mode))
(add-to-list 'auto-mode-alist '("\\.md\\'" . markdown-mode))
(put 'upcase-region 'disabled nil)
(put 'downcase-region 'disabled nil)
